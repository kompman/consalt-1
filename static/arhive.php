<?php

$html=file_get_contents("http://127.0.0.1:8000/");

$FileName = "1.html";
$fp = fopen($FileName, "w");
fwrite($fp, $html);
fclose($fp);
//print_r($html);
echo extension_loaded('zip');
$zip = new ZipArchive(); // подгружаем библиотеку zip

$zip_name = time().".zip"; // имя файла

if($zip->open($zip_name, ZIPARCHIVE::CREATE)!==TRUE)
{
$error .= "* Sorry ZIP creation failed at this time";

}

$zip->addFile($FileName);
$zip->close();

?>