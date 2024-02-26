use std::fs::File;
use std::io::Write;
use std::process::Command;
use std::process::Stdio;

fn main() {
    let mut q1 = 0;
    let mut q2 = 0;
    let mut q3 = 0;
    let mut q4 = 0;

    while q4 < 256 {
        let mut output_file: File = File::options().append(true).open("output.txt").unwrap();
        q1 += 1;
        if q1 > 255 {
            q1 = 0;
            q2 += 1
        }
        if q2 > 255 {
            q2 = 0;
            q3 += 1
        }
        if q3 > 255 {
            q3 = 0;
            q4 += 1
        }
        let addr = format!("{q4}.{q3}.{q2}.{q1}");
        // Create a new file to which the output will be redirected

        let mut command = Command::new("ping");

        // Specify the input file
        command
            .arg(addr)
            .stdout(output_file)
            .spawn()
            .expect("Unreachable");

        //.arg("1>>output.txt")
    }
    //writeln!(&mut output_file, output,.expect("ERROR APPENDING FILE");
}
