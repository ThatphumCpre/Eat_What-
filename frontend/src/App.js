import './App.css';
import FoodCard from './component/FoodCard';
import NavBar from './component/NavBar'


function App() {
  document.title = "กินอะไรดี ?"
  document.body.classList.add('bg-slate-50')
  return (
    <div className='bg-slate-50 ' >
      <div className='mb-2' > 
          <NavBar />
      </div>
      <div className=' p-50 m-auto w-1/2'>
          <h1 className='p-50 ml-50'></h1>
          <FoodCard />
      </div>
    </div>
  );
}

export default App;
