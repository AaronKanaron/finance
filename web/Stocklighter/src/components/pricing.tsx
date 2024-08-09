import React from "react";
import "./pricing.scss"
import Label from "./label";
import CTAButton from "./buttons";

interface PriceProps {
    value: number,
    currency: string,
    currencychar: string,
    originalValue: number,
    trailing: string,
}

interface State {
    isOpen: boolean;
}

class Pricing extends React.PureComponent<{}, State> {
    constructor(props: {}) {
        super(props)
        this.state = {
            isOpen: false,
        };
    }

    handleToggle = (event: React.SyntheticEvent<HTMLDetailsElement>): void => {
        const isNowOpen = (event.target as HTMLDetailsElement).open;
        this.setState({ isOpen: isNowOpen });
    }

    Price = (props: PriceProps) => {
        return (
            <p className="price">
                <span className="currency-char">{props.currencychar}</span>
                <span className="value">{props.value}</span>
                <span className="currency">{props.currency}</span>
                <del className="original-price">
                    <span className="original-currencychar">
                        $
                    </span>
                    <span className="original-value">
                        {props.originalValue}
                    </span>
                </del>
                <span className="trailing-text">
                    {props.trailing}
                </span>
            </p>
        );
    }

    render() {
        return(
            <div className="pricing-options">
                <div className="pricing-options--item">
                    <Label label="Cheapest" id={"n1"}/>
                    <h3>Stocklite</h3>
                    <p className="description">Our most basic model, satisfies users with small, simple portfolios.</p>
                    <this.Price value={5} currency="USD" currencychar="$" originalValue={10} trailing="per month / 60 per month"/>
                    <div className="actions">
                        <CTAButton link="/" label="Buy now" primary={true} arrow={true} block={true}/>
                        {/* <CTAButton link="/" label="Contact sales" primary={false} arrow={true} block={true}/> */}
                    </div>
                    <div className="feature-list">
                        <details className="accordion" open={this.state.isOpen} onToggle={this.handleToggle}>
                            <summary className="accordion__summary">
                                <h4>
                                    <svg aria-hidden="true" focusable="false" role="img" className="chevron" viewBox="0 0 16 16" width="16" height="16" fill="currentColor"><path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path></svg>
                                    What's included
                                </h4>
                            </summary>
                            <section className="accordion__content">
                                <ul>
                                    <li>
                                        <svg aria-hidden="false" focusable="false" aria-label="Includes" role="img" viewBox="0 0 16 16" width="16" height="16" fill="var(--color-accent-primary)"><path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path></svg>
                                        2 usable ticker slots
                                    </li>
                                    <li>
                                        <svg aria-hidden="false" focusable="false" aria-label="Includes" role="img" viewBox="0 0 16 16" width="16" height="16" fill="var(--color-accent-primary)"><path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path></svg>
                                        Real-time notifications of buy and sell nodes
                                    </li>
                                    <li>
                                        <svg aria-hidden="false" focusable="false" aria-label="Includes" role="img" viewBox="0 0 16 16" width="16" height="16" fill="var(--color-accent-primary)"><path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path></svg>
                                        Access to the lightweight accurate SMA model
                                    </li>
                                </ul>
                            </section>
                        </details>
                    </div>
                </div>
                <div className="pricing-options--item">
                    <Label label="Recommended" id={"n2"}/>
                    <h3>Stocklighter</h3>
                    <p className="description">The regular choice, satisfies most users with a regular portfolio.</p>
                    <this.Price value={10} currency="USD" currencychar="$" originalValue={20} trailing="per month / 120 per year"/>
                    <div className="actions">
                        <CTAButton link="/" label="Buy now" primary={true} arrow={true} block={true}/>
                        {/* <CTAButton link="/" label="Contact sales" primary={false} arrow={true} block={true}/> */}
                    </div>
                    <div className="feature-list">
                        <details className="accordion" open={this.state.isOpen} onToggle={this.handleToggle}>
                            <summary className="accordion__summary">
                                <h4>
                                    <svg aria-hidden="true" focusable="false" role="img" className="chevron" viewBox="0 0 16 16" width="16" height="16" fill="currentColor"><path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path></svg>
                                    What's included
                                </h4>
                            </summary>
                            <section className="accordion__content">
                                <ul>
                                    <li>
                                        <svg aria-hidden="false" focusable="false" aria-label="Includes" role="img" viewBox="0 0 16 16" width="16" height="16" fill="var(--color-accent-primary)"><path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path></svg>
                                        Everything included in Stocklite plus:
                                    </li>
                                    <li>
                                        <svg aria-hidden="false" focusable="false" aria-label="Includes" role="img" viewBox="0 0 16 16" width="16" height="16" fill="var(--color-accent-primary)"><path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path></svg>
                                        6 additional ticker slots
                                    </li>
                                    <li>
                                        <svg aria-hidden="false" focusable="false" aria-label="Includes" role="img" viewBox="0 0 16 16" width="16" height="16" fill="var(--color-accent-primary)"><path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path></svg>
                                        Our heavyweight AI-powered performance predictor assignable to one ticker 
                                    </li>
                                </ul>
                            </section>
                        </details>
                    </div>
                </div>
                <div className="pricing-options--item">
                    <Label label="Best Performance" id={"n3"}/>
                    <h3>Stocklightning</h3>
                    <p className="description">Our most robust model, designed for people who want to maximize their profit with minor involvement.</p>
                    <this.Price value={20} currency="USD" currencychar="$" originalValue={25} trailing="per month / 240 per year"/>
                    <div className="actions">
                        <CTAButton link="/" label="Buy now" primary={true} arrow={true} block={true}/>
                        {/* <CTAButton link="/" label="Contact sales" primary={false} arrow={true} block={true}/> */}
                    </div>
                    <div className="feature-list">
                        <details className="accordion" open={this.state.isOpen} onToggle={this.handleToggle}>
                            <summary className="accordion__summary">
                                <h4>
                                    <svg aria-hidden="true" focusable="false" role="img" className="chevron" viewBox="0 0 16 16" width="16" height="16" fill="currentColor"><path d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"></path></svg>
                                    What's included
                                </h4>
                            </summary>
                            <section className="accordion__content">
                                <ul>
                                    <li>
                                        <svg aria-hidden="false" focusable="false" aria-label="Includes" role="img" viewBox="0 0 16 16" width="16" height="16" fill="var(--color-accent-primary)"><path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path></svg>
                                        Everything included in Stocklighter plus:
                                    </li>
                                    <li>
                                        <svg aria-hidden="false" focusable="false" aria-label="Includes" role="img" viewBox="0 0 16 16" width="16" height="16" fill="var(--color-accent-primary)"><path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path></svg>
                                        UNLIMITED ticker slots!
                                    </li>
                                    <li>
                                        <svg aria-hidden="false" focusable="false" aria-label="Includes" role="img" viewBox="0 0 16 16" width="16" height="16" fill="var(--color-accent-primary)"><path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path></svg>
                                        Complete use of all our models
                                    </li>
                                    <li>
                                        <svg aria-hidden="false" focusable="false" aria-label="Includes" role="img" viewBox="0 0 16 16" width="16" height="16" fill="var(--color-accent-primary)"><path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path></svg>
                                        Ability to connect your Avanza account and perform automatic trades
                                    </li>
                                </ul>
                            </section>
                        </details>
                    </div>
                </div>
            </div>
        )
    }
}

export default Pricing;