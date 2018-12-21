<?php
/* 创建一个要计算哈希值的文件 */
file_put_contents('examplde.txt', 'The quick brown fox jumped over the lazy dog.');

echo hash_file('md5', 'example.txt');
?>
