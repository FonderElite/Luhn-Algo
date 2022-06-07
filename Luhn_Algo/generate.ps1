$i = 0;
$luhnAlgoLoc = Read-Host -Prompt 'Directory Location of Luhn-Algo'
python "$luhnAlgoloc\Luhn_Algo\banner.py"
 for($i = 0; $i -lt $param; $i++){ 
   python "$luhnAlgoloc\Luhn_Algo\luhn_prototype.py"
}

