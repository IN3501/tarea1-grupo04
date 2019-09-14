addEventListener('load',inicio,false);

function inicio()
{
  document.getElementById('age').addEventListener('change',cambioage,false);
}

function cambioage()
{    
document.getElementById('eda').innerHTML=document.getElementById('age').value;
}
