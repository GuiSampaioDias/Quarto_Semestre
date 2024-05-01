import React, {useState} from 'react';

function Contador() {
  
  const [contador, setContador] = useState(0);
  function increment(){
    setContador(contador+1);
  }


  return (
    <div className="Contador">
      <p>
      <input type="button" value="Clique" onClick={increment} />
      </p>
      <p>{contador}</p> cliques!
    </div>
  );
}
export default Contador;