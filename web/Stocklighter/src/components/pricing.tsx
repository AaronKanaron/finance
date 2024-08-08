import React from "react";
import "./pricing.scss"
import Label from "./label";

interface PriceProps {
    value: number,
    currency: string,
    currencychar: string,
    originalValue: number,
}

class Pricing extends React.PureComponent {

    Price = (props: PriceProps) => {
        return (
            <p className="price">
                <span className="currency-char">{props.currencychar}</span>
                <span className="value">{props.value}</span>
                <span className="currency">{props.currency}</span>
                <del className="original-price">
                    <span className="original-currencychar">
                        {props.currencychar}
                    </span>
                    <span className="original-value">
                        {props.originalValue}
                    </span>
                </del>
                <span className="trailing-text">
                    per month / 240 per year
                </span>
            </p>
        );
    }

    render() {
        return(
            <div className="pricing-options">
                <div className="pricing-options--item">
                    <Label label="Cheapest" color="#ff80c8"/>
                    <h3>Stocklite</h3>
                    <p>Our most basic model, satisfies users with small, simple portfolios.</p>
                    <this.Price value={20} currency="USD" currencychar="$" originalValue={10}/>
                </div>
                <div className="pricing-options--item">
                    <Label label="Recommended" color="#fd8c73"/>
                    <h3>Stocklighter</h3>
                    <p>The regular choice, satisfies most users with a regular portfolio.</p>
                    <this.Price value={20} currency="USD" currencychar="$" originalValue={10}/>
                </div>
                <div className="pricing-options--item">
                    <Label label="Best Performance" color="#9AA4FF"/>
                    <h3>Stocklightning</h3>
                    <p className="description">Our most robust model, designed for people who want to maximize their profit with minor involvement.</p>
                    <this.Price value={20} currency="USD" currencychar="$" originalValue={10}/>

                </div>
            </div>
        )
    }
}

export default Pricing;