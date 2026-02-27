import './BuildingCard.css';

interface BuildingData {
    name: string;
    rooms_available: number;
    building_file?: string;
    building_picture?: string;
}

interface BuildingCardProps {
    building: BuildingData;
}

const BuildingCard = ({ building }: BuildingCardProps) => {
    const imagePath = building.building_picture || building.building_file;

    let cleanImagePath = imagePath?.startsWith('./')
        ? `/assets/${imagePath.substring(2)}`
        : `/assets/${imagePath}`;

    if (cleanImagePath === '/assets/anitb.webp') {
        cleanImagePath = '/assets/anitab.webp';
    }

    return (
        <div className="building-card">
            <div
                className="card-image-bg"
                style={{ backgroundImage: `url(${cleanImagePath})` }}
            >
                <div className="status-pill">
                    <span className="status-dot"></span>
                    {building.rooms_available} rooms available
                </div>
            </div>
            <div className="card-footer">
                <h3 className="building-name">{building.name}</h3>
            </div>
        </div>
    );
};

export default BuildingCard;
