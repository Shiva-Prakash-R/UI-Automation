package com.Api.test;

import static io.restassured.RestAssured.given;
import static org.hamcrest.Matchers. *;

import io.restassured.RestAssured;
import io.restassured.path.json.JsonPath;

public class PostApiNewUsers {
	
public static void main(String[] args) {
		
		RestAssured.baseURI = "https://reqres.in/";
		
		String response = given().log().all().header("Content-Type", "application/json").body(payLoad.AddPlace())
		.when().post("api/users").then().log().all().assertThat().statusCode(201).body("name", equalTo ("morpheus"))
		.body("job", equalTo ("leader")).header("server", "cloudflare").extract().response().asString();
		
		System.out.println(response);
		
		// Json extract  
		
		JsonPath js = new JsonPath(response);
		
		String CreatedAt = js.getString("createdAt");
		
		System.out.println("Created Date and Time : " + CreatedAt);
		
	}

}
