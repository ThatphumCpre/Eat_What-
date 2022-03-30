import React, { useEffect, useState } from "react";

const TodosContext = React.createContext({
    todos: [], fetchTodos: () => {}
    })
  
export default function Todos() {
const [todos, setTodos] = useState([])
const fetchTodos = async () => {
    const response = await fetch("http://localhost:8000/foods")
    const todos = await response.json()
    setTodos(todos.data)
}

return (
    <TodosContext.Provider value={{todos, fetchTodos}}>
        <div className="w-3/4 max-w-xl ml-auto mr-auto rounded overflow-hidden shadow-lg content-center ">
        <img className="w-full img-banner" src={todos.img} alt="Sunset in the mountains" />
        <div className="px-6 py-4">
            <div className="font-bold text-xl mb-2">{todos.menu}</div>
            <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full" onClick={fetchTodos}>
                สุ่มอาหารใหม่
            </button>
        </div>
        <div className="px-6 pt-4 pb-2">
            <span className="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">{todos.type}</span>
        </div>
    </div>
    </TodosContext.Provider>
)
}