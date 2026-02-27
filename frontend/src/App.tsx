import { useState } from 'react'
import data from './data.json'
import './App.css'
import Navbar from './components/Navbar/Navbar'
import FilterBar from './components/FilterBar/FilterBar'
import BuildingGrid from './components/BuildingGrid/BuildingGrid'

interface BuildingData {
  name: string;
  rooms_available: number;
  building_file?: string;
  building_picture?: string;
}

function App() {
  const [buildings] = useState<BuildingData[]>(data as BuildingData[])

  return (
    <div className="app-container">
      <Navbar />
      <hr className="divider" />
      <main className="main-content">
        <FilterBar />
        <BuildingGrid buildings={buildings} />
      </main>
    </div>
  )
}

export default App
