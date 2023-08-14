import fs from "fs-extra";
import { glob } from "glob";
import path from "path"
import inquirer from "inquirer"
import type { InputQuestion, ListQuestion } from "inquirer"

function listFilesAndFoldersIn(srcDir: string): void {
    fs.readdir(srcDir, (err: Error, files: string[]) => {
        if (err) {
            console.error(err);
            return;
        }
        for (const name of files) {
            console.log(name);
        }
    });
}
// const srcDir: string = process.argv[2];
// listFilesAndFoldersIn(srcDir)

const inFilesToEscape = (fileName: string) => {
    const skipDirectories = ["dist"];
    const inSkipDirectories = skipDirectories.some(directory =>
        fileName.match(RegExp(`/?${directory}/`))
    );
    if (inSkipDirectories) return true;
    const skipFileExtensions = ["map", "json"];
    const inSkipFileExtensions = skipFileExtensions.some(fileExtension => {
        const output = fileName.match(RegExp(`\.${fileExtension}$`, "m"));
        return output === null;
    });
    if (inSkipFileExtensions) return true;
    return false;
};

function copyFilesFrom(srcDirP: string, destDir: string) {
    glob(`${srcDirP}/**/*.*`, { ignore: ["node_modules/**", "*.json", "dist/**"] }).then(
        async (arrMatchedFileNames: string[]) => {
            // const filesToProcess = arrMatchedFileNames.filter(fileName => !inFilesToEscape(fileName))
            for (const index in arrMatchedFileNames) {
                const srcPath = arrMatchedFileNames[index]
                const srcDir = path.dirname(srcPath)
                const dstPath = srcPath.replace(srcDir, destDir)
                const dstDir = path.dirname(dstPath)
                const fileStatus = await fs.stat(srcPath)
                console.log(path.dirname(srcPath))
                fs.ensureDir(dstDir, async (err) => {
                    if (err) {
                        console.log(err)
                        return
                    }
                    console.log(fileStatus.isFile())
                    fs.copy(srcPath, dstPath, (err1) => {
                        if (err1) {
                            console.log(err)
                            return
                        }
                        console.log(`created new file in ${dstDir}`)
                    })
                })
            }
        }
    );
}
// const [srcDir, destDir] = process.argv.slice(2)
// copyFilesFrom(srcDir, destDir)

// Exercises
// Q1
function Q1() {
    const red = () => {
        console.log('RED')
    }

    const green = (func: () => void) => {
        console.log('GREEN')
        func()
    }

    const blue = (left: (inputFunc: () => void) => void, right: () => void) => {
        console.log('BLUE')
        left(right)
    }
    blue(green, red)
}

// Q2



function Q2() {
    type VoidFunc = () => void
    type LeftFunc = (inputFunc: VoidFunc) => void

    const blue2: (leftFunc: LeftFunc, rightFunc: VoidFunc) => void = (left, right) => {
        console.log('BLUE')
        left(right)
    }
    blue2(
        (callback) => {
            console.log('GREEN')
            callback()
        },
        () => console.log('RED')
    )
}

// Q3
async function Q3() {
    // console.log(process.argv)
    // if (process.argv.length == 2) {
    console.log(`
Help:
    Synopsis:
            node dist/chapter2.js [SRC_DIRECTORY] [DEST_DIRECTORY]

    Description:
            Copies files from SRC_DIRECTORY to DEST_DIRECTORY
`)
    let srcDirQuestion: InputQuestion = {
        name: "src_dir",
        message: "Source directory",
        default: "."
    }
    let destDirQuestion: InputQuestion = {
        name: "dest_dir",
        message: "Destination directory",
        default: "dest"
    }
    const answers = await inquirer.prompt([srcDirQuestion, destDirQuestion], {})
    const { src_dir: srcDir, dest_dir: destDir } = answers
    console.log(srcDir, destDir)
    if (!fs.existsSync(srcDir)) {
        console.error("Invalid SRC_DIRECTORY path")
        return
    }
    copyFilesFrom(srcDir, destDir)
}



function Q4() {
    const people = [
        { personal: 'Jean', family: 'Jennings' },
        { personal: 'Marlyn', family: 'Wescoff' },
        { personal: 'Ruth', family: 'Lichterman' },
        { personal: 'Betty', family: 'Snyder' },
        { personal: 'Frances', family: 'Bilas' },
        { personal: 'Kay', family: 'McNulty' }
    ]
    const result = people.filter(({ personal, family }) => ['j', 'r', 'f'].some(char => personal.toLowerCase().startsWith(char)))
    console.log(result)
}

async function countLines() {
    const filesNames = process.argv.slice(2, process.argv.length)
    for (let i = 0; i < filesNames.length; i++) {
        const filePath = filesNames[i]
        const status = await fs.stat(filePath)
        if (!status.isFile()) {
            console.log(`Cannot found file with name ${filePath}`)
            continue
        }
        while (await fs.read)
    }

}
countLines()
/**
 * Function Genetrates CLI Prompt
 */
async function cliPrompt() {
    let question: ListQuestion = {
        type: 'list',
        name: "select_ques",
        message: "Which question you want to execute ?",
        default: "Q1",
        choices: ["Q1", "Q2", "Q3", "Q4", "Exit"]
    }
    const answers: { [key: string]: string } = await inquirer.prompt([question], {})
    switch (answers.select_ques) {
        case 'Q1':
            Q1()
            break
        case 'Q2':
            Q2()
            break
        case 'Q3':
            Q3()
            break
        case 'Q4':
            Q4()
        case "Exit":
            process.exit()
        default:
            console.error("No such question found")
    }
}
// cliPrompt()