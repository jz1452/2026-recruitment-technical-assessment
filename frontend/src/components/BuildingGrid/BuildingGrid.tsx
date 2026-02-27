import './BuildingGrid.css';
import BuildingCard from '../BuildingCard/BuildingCard';

interface BuildingData {
    name: string;
    rooms_available: number;
    building_file?: string;
    building_picture?: string;
}

interface BuildingGridProps {
    buildings: BuildingData[];
}

const BuildingGrid = ({ buildings }: BuildingGridProps) => {
    return (
        <div className="building-grid">
            {buildings.map((building, index) => (
                <BuildingCard key={index} building={building} />
            ))}
        </div>
    );
};

export default BuildingGrid;
