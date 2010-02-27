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

/**
  * Given a value, make a string that length in KBytes up to a 
  * maximum of 1MByte.
  *
  */
function makeAString($length) {
  $chars = 'ABCDEFGHJKLMNPQRSTUVWXYZabcdefghjkmstringqrstuvwxyz';
  $l = strlen( $chars ) - 1;

  $digit = mt_rand(0, $length - 1);
  $genlength = 1024 * mt_rand(1, 1024) * $length;
  $string = '';
  for ( $i = 0; $i < $genlength; $i++ ) {
    $string .= $i == $digit ? chr( mt_rand(48, 57) ) : $chars{ mt_rand(0, $l)};
  }
  return $string;
}

function grabBytes() {
  $genlength = mt_rand(1024, 1024*1024);
  $string = file_get_contents("/dev/urandom", 0, NULL, -1, $genlength);
  return $string;
}

function randData() {
  $arr;
  for ($i=0; $i<100; $i++) {
    $tmp_str = grabBytes();
    $arr[i] = array(md5($str) => $tmp_str);
  }
  return $arr;
}

?>
