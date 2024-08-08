import { FC, PropsWithChildren } from 'react'
import "./label.scss"

interface LabelProps extends PropsWithChildren<any> {
    label: string,
    color1?: string,
    color2?: string,
    color?: string,
    combination?: string,
}


const Label: FC<LabelProps> = (props): JSX.Element => {
    let styleColor = {}
    if (props.color1) {
        styleColor = {"--start-color": props.color1, "--end-color": props.color2}
    } else if (props.color) {
        styleColor = {"--start-color": props.color, "--end-color": props.color}
    } else {
        styleColor = {}
    }

    return (
        <span className="label" style={styleColor as React.CSSProperties}>
            <span className="label--content">
                {props.label}
            </span>
        </span>
    );
}

export default Label;