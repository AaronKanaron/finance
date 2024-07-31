import React, { useRef, useEffect } from 'react';
import { mat4 } from 'gl-matrix';

const WebGLCanvas = () => {
  const canvasRef = useRef(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    const gl = canvas.getContext('webgl');

    if (!gl) {
      console.error('WebGL not supported');
      return;
    }

    // Vertex shader program
    const vsSource = `
      attribute vec4 aVertexPosition;
      uniform mat4 uModelViewMatrix;
      uniform mat4 uProjectionMatrix;
      varying vec2 vPosition;
      void main() {
        gl_Position = uProjectionMatrix * uModelViewMatrix * aVertexPosition;
        vPosition = aVertexPosition.xy;
      }
    `;

    // Fragment shader program
    const fsSource = `
      precision mediump float;
      varying vec2 vPosition;
      uniform float uTime;
      
      vec3 chromaticAberration(vec2 uv) {
        float aberrationAmount = 0.01 * (1.0 - smoothstep(0.0, 0.8, 1.0 - length(uv)));
        vec2 uvR = uv - aberrationAmount;
        vec2 uvB = uv + aberrationAmount;
        return vec3(
          smoothstep(0.03, 0.01, min(abs(uvR.x), abs(uvR.y))),
          smoothstep(0.03, 0.01, min(abs(uv.x), abs(uv.y))),
          smoothstep(0.03, 0.01, min(abs(uvB.x), abs(uvB.y)))
        );
      }
      
      void main() {
        vec3 color = chromaticAberration(vPosition);
        gl_FragColor = vec4(color, 1.0);
      }
    `;

    // Initialize a shader program
    const shaderProgram = initShaderProgram(gl, vsSource, fsSource);

    // Collect all the info needed to use the shader program
    const programInfo = {
      program: shaderProgram,
      attribLocations: {
        vertexPosition: gl.getAttribLocation(shaderProgram, 'aVertexPosition'),
      },
      uniformLocations: {
        projectionMatrix: gl.getUniformLocation(shaderProgram, 'uProjectionMatrix'),
        modelViewMatrix: gl.getUniformLocation(shaderProgram, 'uModelViewMatrix'),
        time: gl.getUniformLocation(shaderProgram, 'uTime'),
      },
    };

    // Create the grid lines
    const buffers = initBuffers(gl);

    // Animation loop
    let then = 0;
    function render(now) {
      now *= 0.001;  // convert to seconds
      const deltaTime = now - then;
      then = now;

      drawScene(gl, programInfo, buffers, now);

      requestAnimationFrame(render);
    }
    requestAnimationFrame(render);

  }, []);

  return <canvas ref={canvasRef} width={800} height={600} className='web-gl-canvas'/>;
};

// Initialize a shader program, so WebGL knows how to draw our data
function initShaderProgram(gl, vsSource, fsSource) {
  const vertexShader = loadShader(gl, gl.VERTEX_SHADER, vsSource);
  const fragmentShader = loadShader(gl, gl.FRAGMENT_SHADER, fsSource);

  const shaderProgram = gl.createProgram();
  gl.attachShader(shaderProgram, vertexShader);
  gl.attachShader(shaderProgram, fragmentShader);
  gl.linkProgram(shaderProgram);

  if (!gl.getProgramParameter(shaderProgram, gl.LINK_STATUS)) {
    console.error('Unable to initialize the shader program: ' + gl.getProgramInfoLog(shaderProgram));
    return null;
  }

  return shaderProgram;
}

function loadShader(gl, type, source) {
  const shader = gl.createShader(type);
  gl.shaderSource(shader, source);
  gl.compileShader(shader);

  if (!gl.getShaderParameter(shader, gl.COMPILE_STATUS)) {
    console.error('An error occurred compiling the shaders: ' + gl.getShaderInfoLog(shader));
    gl.deleteShader(shader);
    return null;
  }

  return shader;
}

function initBuffers(gl) {
  const positions = [];
  const gridSize = 20;
  const spacing = 2 / gridSize;

  // Create vertical lines
  for (let i = 0; i <= gridSize; i++) {
    const x = i * spacing - 1;
    positions.push(x, -1, 0);
    positions.push(x + 0.1, 1, 0); // Slight skew to the right
  }

  // Create horizontal lines
  for (let i = 0; i <= gridSize; i++) {
    const y = i * spacing - 1;
    positions.push(-1, y, 0);
    positions.push(1, y - 0.1, 0); // Slight skew downwards
  }

  const positionBuffer = gl.createBuffer();
  gl.bindBuffer(gl.ARRAY_BUFFER, positionBuffer);
  gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(positions), gl.STATIC_DRAW);

  return {
    position: positionBuffer,
    count: positions.length / 3
  };
}

function drawScene(gl, programInfo, buffers, time) {
  gl.clearColor(0.0, 0.0, 0.0, 1.0);
  gl.clear(gl.COLOR_BUFFER_BIT);

  const fieldOfView = 45 * Math.PI / 180;
  const aspect = gl.canvas.clientWidth / gl.canvas.clientHeight;
  const zNear = 0.1;
  const zFar = 100.0;
  const projectionMatrix = mat4.create();

  mat4.perspective(projectionMatrix, fieldOfView, aspect, zNear, zFar);

  const modelViewMatrix = mat4.create();
  mat4.translate(modelViewMatrix, modelViewMatrix, [-0.0, 0.0, -6.0]);

  gl.bindBuffer(gl.ARRAY_BUFFER, buffers.position);
  gl.vertexAttribPointer(programInfo.attribLocations.vertexPosition, 3, gl.FLOAT, false, 0, 0);
  gl.enableVertexAttribArray(programInfo.attribLocations.vertexPosition);

  gl.useProgram(programInfo.program);

  gl.uniformMatrix4fv(programInfo.uniformLocations.projectionMatrix, false, projectionMatrix);
  gl.uniformMatrix4fv(programInfo.uniformLocations.modelViewMatrix, false, modelViewMatrix);
  gl.uniform1f(programInfo.uniformLocations.time, time);

  gl.drawArrays(gl.LINES, 0, buffers.count);
}


export default WebGLCanvas;