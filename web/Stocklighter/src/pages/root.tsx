import './root.scss'
import CTAButton from '../components/buttons'
import stockImage from "../assets/stocks2.png"
import Label from '../components/label'
import Navigator from '../components/navbar'
import Pricing from '../components/pricing'

export default function Root() {
    return (
        <>
            <Navigator></Navigator>
            <section className='section section--hero'>
                <div className="section--container">
                    <section className="heading">
                        <Label label="Use code 'first-timer' for 15% off first purchase" color1='#ffc1ba' color2='#7ee787'/>
                        <h1 className='heading-title'>
                            Quantitative analysis for everyday people
                        </h1>
                        <div className="hero-cta">
                            <CTAButton link="/plans" arrow={true} primary={true} label="Get started with Stocklighter" />
                        </div>
                    </section>
                    <div className="hero-visual">
                        <div className="hero-visual--image-container">
                            <img className="hero-image" src={stockImage} alt="" />
                        </div>
                    </div>
                </div>
                <div className="cover" />
            </section>
            <section className='section section--level-1'>
                <div className="section--container">
                    <header className="section-intro">
                        <Label label="Fundamentals"/>
                        <h2>Advance without too much commitment.</h2>
                        
                    </header>
                    <p>
                            Lorem quis occaecat non consectetur aliqua do sint minim nisi qui laboris. Consequat exercitation ad proident laborum nulla proident. Aute mollit nisi fugiat ullamco. Adipisicing excepteur aute enim est. Dolor anim esse aute qui nostrud irure Lorem dolor ad nostrud proident consequat aliqua commodo.

Amet quis esse Lorem fugiat tempor dolor. Est laboris nisi mollit id eu mollit excepteur. Minim cillum elit ullamco ad elit amet aliquip sit cillum. Do culpa non reprehenderit enim culpa ea consequat. Ex deserunt nulla anim laborum. Do id est voluptate veniam irure consequat. Sit et deserunt laboris adipisicing ut culpa anim velit non nisi eiusmod aute.

Labore sint nostrud et tempor cillum cillum sunt aute pariatur. Ut enim in esse sit veniam et dolore et proident occaecat amet. Deserunt enim ad ut est enim sint aute elit incididunt minim ipsum occaecat proident. Sit irure nisi amet mollit consectetur ut officia sit. Enim mollit elit in officia laborum quis consequat esse aliqua. Consequat exercitation voluptate nisi velit laboris fugiat do cillum. Tempor aute deserunt quis sit laborum do dolor.

Excepteur nisi nulla sint nostrud officia fugiat id minim quis velit ex. Aute aliqua deserunt sunt laboris commodo eiusmod qui ipsum velit id. Labore minim sit commodo excepteur nisi irure laborum deserunt. Tempor quis do occaecat anim ipsum elit id sit dolor Lorem occaecat reprehenderit. Id ullamco non pariatur et ut et.

Est consequat ipsum magna anim ullamco enim ea labore aliquip deserunt dolor. Sit exercitation ullamco irure ipsum officia quis amet. Dolore excepteur id cillum officia consectetur laborum aliquip cillum.
                        </p>
                </div>
            </section>
            <section className='section section--level-2'>
                <div className="section--container">
                    <header className="section-intro center">
                        <Label label='Reduced price' combination='red'/>
                        <h2>Start your journey now</h2>
                        <p>
                            12 million other users use Stocklighter reguarly to boost their performance, get insight and growth their fortune. Now is your chance to do the same.
                        </p>
                    </header>
                    <Pricing></Pricing>
                </div>
            </section>

        </>
    )
}