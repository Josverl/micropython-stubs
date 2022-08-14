
foreach ($port in "rp2","stm32","esp32","esp8266"){
    pip install micropython-$port-stubs==1.17.*  -t publish\micropython-v1_17-$port-stubs --upgrade
}

foreach ($port in "rp2","stm32","esp32","esp8266"){
    pip install micropython-$port-stubs==1.18.*  -t publish\micropython-v1_18-$port-stubs --upgrade
}

foreach ($port in "rp2","stm32","esp32","esp8266"){
    pip install micropython-$port-stubs==1.19.1.*  -t publish\micropython-v1_19_1-$port-stubs --upgrade
}


