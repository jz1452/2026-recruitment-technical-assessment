import './FilterBar.css';

const FilterBar = () => {
    return (
        <div className="filter-bar">
            <button className="filter-btn outline-btn">
                <span className="material-symbols-outlined icon-small">filter_alt</span>
                Filters
            </button>

            <div className="search-container">
                <span className="material-symbols-outlined search-icon">search</span>
                <input
                    type="text"
                    placeholder="Search for a building..."
                    className="search-input"
                />
            </div>

            <button className="filter-btn outline-btn">
                <span className="material-symbols-outlined icon-small">sort</span>
                Sort
            </button>
        </div>
    );
};

export default FilterBar;
