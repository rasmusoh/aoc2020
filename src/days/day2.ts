async function main() {
    run(solve, '/data/day2.test.txt', 'solution-test');
    run(solve, '/data/day2.txt', 'solution');
}


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

class PasswordPolicy {
    constructor(public from: number, public to: number, public char: string, public pw: string) {
    }
    isValid() {
        const count = this.getOccurences();
        return count >= this.from && count <= this.to;
    }
    getOccurences() {
        return (this.pw.match(this.char) || []).length;
    }
    print() {
        return `${this.from}-${this.to}, c:${this.char} pw:${this.pw} valid:${this.isValid()}`;
    }
}


function solve(data: string): any {
    const parse = (line: string): PasswordPolicy => {
        const tokens = line.match(/(\d+)-(\d+) (\w): (\w+)/g)
        const from = parseInt(tokens[0]);
        const to = parseInt(tokens[1]);
        const char = tokens[2];
        const password = tokens[3];
        return new PasswordPolicy(from, to, char, password);
    };
    return data.split('\n').filter(x => x).map(parse)//.map(x => x.print());
}

main();

