<?php

// CDDL HEADER START
//
// The contents of this file are subject to the terms of the
// Common Development and Distribution License (the "License").
// You may not use this file except in compliance with the License.
//
// See LICENSE.txt included in this distribution for the specific
// language governing permissions and limitations under the License.
//
// When distributing Covered Code, include this CDDL HEADER in each
// file and include the License file at LICENSE.txt.
// If applicable, add the following below this CDDL HEADER, with the
// fields enclosed by brackets "[]" replaced with your own identifying
// information: Portions Copyright [yyyy] [name of copyright owner]
//
// CDDL HEADER END

include 'common.php';

// connect to the memcached servers from the envvar
$memcache = new Memcache;
$servers = getenv('MEMCACHED_SERVERS');
echo $servers;
echo "\n";
$parsed = preg_split("/,/", $servers);
foreach($parsed as $indiv) {
  $system = preg_split("/:/", $indiv);
  $memcache->addServer($system[0], $system[1]);
}

$tmp_object = new stdClass;
$tmp_object->str_attr = 'test';
$tmp_object->int_attr = 123;

$memcache->set('key', $tmp_object, false, 10) or die ("Failed to save data at the server");
echo "Store data in the cache (data will expire in 10 seconds)<br/>\n";

$get_result = $memcache->get('key');
echo "Data from the cache:<br/>\n";

// var_dump(randData());
$data = randData();


?>
