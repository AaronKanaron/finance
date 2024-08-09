/* main.tsx */

/* Package Imports */
import React from 'react'
import ReactDOM from 'react-dom/client'
import {
  createBrowserRouter,
  RouterProvider
} from "react-router-dom"

/* Pages import */
import Root from './pages/root.tsx'

/* Styles import */
import './styles/globals.scss'

const router = createBrowserRouter([
  {
    path: "/",
    element: <Root />
  },
  {
    path: "/dashboard",
    element: <h1> Hello</h1>
  }
])

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
      <div data-theme="dark">
        <RouterProvider router={router} />
      </div>
  </React.StrictMode>,
)
