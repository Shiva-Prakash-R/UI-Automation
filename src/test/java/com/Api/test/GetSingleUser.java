package com.Api.test;

import io.restassured.RestAssured;
import static io.restassured.RestAssured. *;
import static org.hamcrest.Matchers.*;


public class GetSingleUser {
	
	public static void main(String[] args) {
		
		RestAssured.baseURI = "https://reqres.in/";
		
		given().log().all().header("Content-Type", "application/json").param("id","2")
		.when().get("api/users").then().log().all().assertThat().statusCode(200);
	}

}
