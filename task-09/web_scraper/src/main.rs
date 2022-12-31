use std::error::Error;
use std::io;
use std::process;


use std::fs::File;
use std::io::prelude::*;




fn main() {
    println!("Hello, globe!");
    
    let mut title_vec = Vec::new();
    let mut TFchange_vec = Vec::new();
    
    let mut Price_vec = Vec::new();
    let mut volume_vec = Vec::new();
    let mut marketCap_vec = Vec::new();
    let response = reqwest::blocking::get("https://crypto.com/price",)
    .unwrap()
    .text()
    .unwrap();

   

    let document = scraper::Html::parse_document(&response);


    //////////////////////////////////////////////////////////////////////////
    //title ------------------.-----------------------------------------------

    let title_selector = scraper::Selector::parse("div.css-ttxvk0>p").unwrap();

    let titles = document.select(&title_selector).map(|x| x.inner_html());

    titles
    .zip(1..101)
    .for_each(|(item, number)|title_vec.push(item) ); //let v : Vec<i64> = Vec::new(); 


    ////////////////////////////////////////////////////////////////////////////
    
    
    ///////////////////////////////////////////////////////////////////////////////
    //24hr change working.........................................................

     let  twofour_selector = scraper::Selector::parse("td.css-1b7j986>p").unwrap();

     let  twofour = document.select(&twofour_selector).map(|x| x.inner_html());


     twofour
     .zip(1..101)
     .for_each(|(item, number)| TFchange_vec.push(item));


     //////////////////////////////////////////////////////////////////////////////
     //price......................................................................

     let  price_selector = scraper::Selector::parse("div.css-16q9pr7>div").unwrap();

     let  price = document.select(&price_selector).map(|x| x.inner_html());

    

     price
     .zip(1..101)
     .for_each(|(item, number)| Price_vec.push(item));

     //////////////////////////////////////////////////////////////////////////
     //cap - --------------------------------------------------------------------
     println!("Hello, globe!");
     let  Cap_selector = scraper::Selector::parse("td.css-1nh9lk8").unwrap();

     let  Cap = document.select(&Cap_selector).map(|x| x.inner_html());

     Cap
     .zip(1..101)
     .for_each(
        |(item, number)| 
        
        if(number%2==0){
            volume_vec.push(item)
          
        }else{
           
           marketCap_vec.push(item)

        }
        
        );


        ///////////////////////////////////////////////////////////////////////////////


    
    let mut wtr = csv::Writer::from_path("crypto.csv").unwrap();
    wtr.write_record(&["No.","Name", "Price", "24H-Change","24H-Volume","Market-cap"]).expect("Could not write header.");
  
    
    



    for x in 0..51{     
       
           let i = x;
        //    println!("{}",i);
           let s: String = x.to_string();
           let title=&title_vec[0];
           wtr.write_record([&s,&title_vec[i],&Price_vec[i],&TFchange_vec[i],&volume_vec[i],&marketCap_vec[i]]).expect("Could not create selector.");

    }


   

     


    
    // wtr.flush().expect("Could not close file");
    // println!("Done");

    

    println!("{}",title_vec[0]);
 
    // printing the size of vector
    println!("{ }",title_vec.len());
   
    println!("{ }",TFchange_vec.len());
    println!("{ }",Price_vec.len());
    println!("{ }",volume_vec.len());
    println!("{ }",marketCap_vec.len());

        



    
    }