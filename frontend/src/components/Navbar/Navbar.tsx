import './Navbar.css';

const Navbar = () => {
    return (
        <nav className="navbar">
            <div className="navbar-logo">
                <img
                    src="/assets/freeRoomsLogo.png"
                    alt="Freerooms Logo Icon"
                    className="logo-icon"
                />
                <h1 className="logo-text">Freerooms</h1>
            </div>

            <div className="navbar-actions">
                <button className="icon-btn active">
                    <span className="material-symbols-outlined">search</span>
                </button>
                <button className="icon-btn active-bg">
                    <span className="material-symbols-outlined">grid_view</span>
                </button>
                <button className="icon-btn">
                    <span className="material-symbols-outlined">map</span>
                </button>
                <button className="icon-btn">
                    <span className="material-symbols-outlined">dark_mode</span>
                </button>
            </div>
        </nav>
    );
};

export default Navbar;
