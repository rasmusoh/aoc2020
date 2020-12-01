async function main() {
    run(solve, '/data/day1.test.txt', 'solution-test');
    run(solve, '/data/day1.txt', 'solution');
}
const N_ELEMENTS = 3;

async function run(solveFn: (data: string) => string, inputUrl: string, outputelement: string) {
    try {
        const inputResponse = await fetch(inputUrl);
        const inputData = await inputResponse.text();
        const result = solveFn(inputData);
        document.getElementById(outputelement).innerText = result;
    } catch (e) {
        document.getElementById(outputelement).innerText = e;
    }
}

function solve(data: string): any {
    var numbers = data.split('\n').filter(x => x).map(x => parseInt(x)).sort((a, b) => a - b);
    const blacklist = [];//[1383,262,375];
    const find = (n: number, sum: number): number[] => {
        if (n === 1) {
            for (let i = 0; i < numbers.length; i++) {
                if (numbers[i] === sum) return [numbers[i]];
                if (numbers[i] > sum) return [];
            }
        } else {
            for (let i = 0; i < numbers.length; i++) {
                const result = find(n - 1, sum - numbers[i]);
                if (result.length && !result.includes(numbers[i]) && !blacklist.includes(numbers[i])) {
                    return result.concat(numbers[i]);
                }
            }
        }
        return [];
    }
    const result = find(N_ELEMENTS, 2020);
    return [result, result.reduce((a, b) => a + b), result.reduce((a, b) => a * b)].join(' - ');
}


main();

