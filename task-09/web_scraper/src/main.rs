fn main() {
   
    let response = reqwest::blocking::get(
        "https://crypto.com/pricettps://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc&count=100",
    )
    .unwrap()
    .text()
    .unwrap();

}