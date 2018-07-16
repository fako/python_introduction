<?php
    ini_set('memory_limit', '2048M');
    echo "Start test\n";
    $dataPath = join(DIRECTORY_SEPARATOR, array('data', 'data.json'));

    $t0 = microtime(true);

    $fileContents = file_get_contents($dataPath);

    $data = json_decode($fileContents, true);

    $t1 = microtime(true);

    foreach ($data as $object) {
        $object["top10Buildins"] = array_values($object["top10Buildins"]);
    }
    $json = json_encode(array_values($data));
    file_put_contents($dataPath, $json);

    $t2 = microtime(true);

    $loadingTime = $t1 - $t0;
    $dumpingTime = $t2 - $t1;
    echo "Loading took $loadingTime\n";
    echo "Dumping took $dumpingTime\n";
    echo "End test\n";

?>
