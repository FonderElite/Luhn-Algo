$param = $args[0];
$i = 0;
python "Luhn_Algo\banner.py"
 for($i = 0; $i -lt $param; $i++){ 
   python "Luhn_Algo\luhn_prototype.py"
}

