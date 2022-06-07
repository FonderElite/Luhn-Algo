$i = 0;
$param = $args[0];
python "banner.py"
 for($i = 0; $i -lt $param; $i++){ 
   python "luhn_prototype.py"
}

