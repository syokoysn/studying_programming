fn main() {
    println!("gcd:{}", euclidean_algorithm(1053,234));
}

fn euclidean_algorithm(a: i32, b: i32)-> i32{
    if a%b == 0{ b}
    else{euclidean_algorithm(b,a%b)}
}