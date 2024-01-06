<?php
$user_ip = $_SERVER['REMOTE_ADDR'];
$answer = md5("3" . $user_ip);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta name="referrer" content="same-origin">
    <meta name="referrer" content="no-referrer">
    <title>Stalker-RP UCP Skip</title>

    <style>
        html { font-family: monospace; }
        h1 { font-size: 34pt; }
        button { font-size: 24pt; }
    </style>
</head>
<body>
    <h1>stalker-rp ucp questions skip</h1>
    <form action="https://stalker-rp.net/register?step=2" method="post" rel="noreferrer">
        <? for ($i = 0; $i <= 4; $i++): ?>
            <input type="hidden" name="ans_<?= $i ?>" value="<?= $answer ?>">
            <input type="hidden" name="question_<?= $i ?>" value="29">
        <? endfor; ?>
        <button type="submit" name="continue" value="accept">skip questions</button>
    </form>
</body>
</html>