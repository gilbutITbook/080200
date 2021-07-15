console.log('code starts')

setTimeout(() => {
    console.log('callback executed');
}, 1000);

cpu_bound_task = () => {
    const start = Date.now();
    var elapsed = 0;
    while (elapsed < 5000) {
        const end = Date.now();
        const ms = (end.valueOf() - start.valueOf());
        elapsed = ms;
        sec = ms / 1000;
        if (elapsed % 1000 === 0) {
            console.log(sec + " sec");
        }
    }
}

cpu_bound_task();