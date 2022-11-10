<?php

function open_file($input_file) {
  $lines = file($input_file);
  return $lines;
}


function part_one($input_file) {
  $lines = open_file($input_file);
}

function part_two($input_file) {
  $lines = open_file($input_file);
}


$part_one_answer = part_one("input.txt");
$part_two_answer = part_two("input.txt");

var_dump($part_one_answer);
echo "Answer #1 = $part_one_answer";

var_dump($part_two_answer);
echo "Answer #2 = $part_two_answer";

?>
