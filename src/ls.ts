import fs from "fs-extra"
import glob from "glob"

function listFilesAndFoldersIn(path:string):void {
    fs.readdir(srcDir, (err:Error, files:string[]) => {
    if (err) {
        console.error(err)
        return
    }
    for (const name of files) {
        console.log(name)
    }
})
    
}
const srcDir:string = process.argv[2]
listFilesAndFoldersIn(srcDir)