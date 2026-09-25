import { useEffect, useState } from 'react'
import axios from 'axios'

function App() {
  const [products, setProducts] = useState([]);

  useEffect(()=> {
    axios.get('http://127.0.0.1:8000/api/products/products/').then(response =>{
      setProducts(response.data)
    })
  },[])

  return (
    <div>
      <h1>Django + React Integration</h1>
      <ul>
        {products.map((products) => (
          <li key={products.id}>
            {products.name}<br/>
            {products.description}<br/><br/>
          </li>
        ))}
      </ul>
    </div>
  )
}

export default App
