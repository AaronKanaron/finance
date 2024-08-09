import { FC, PropsWithChildren } from 'react'
import "./label.scss"

interface LabelProps extends PropsWithChildren<any> {
    label: string,
    color1?: string,
    color2?: string,
    color?: string,
    combination?: string,
}


const Label: FC<LabelProps> = ({label, color1, color2, color, ...attributes}): JSX.Element => {
    let styleColor = {}
    if (color1) {
        styleColor = {"--start-color": color1, "--end-color": color2}
    } else if (color) {
        styleColor = {"--start-color": color, "--end-color": color}
    } else {
        styleColor = {}
    }

    return (
        <span className="label" style={styleColor as React.CSSProperties} {...attributes}>
            <span className="label--content">
                {label}
            </span>
        </span>
    );
}

export default Label;