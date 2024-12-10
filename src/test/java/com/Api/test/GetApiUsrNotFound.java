package com.Api.test;

import static io.restassured.RestAssured.given;

import io.restassured.RestAssured;

public class GetApiUsrNotFound {
	
public static void main(String[] args) {
		
		RestAssured.baseURI = "https://reqres.in/";
		
		given().log().all().header("Content-Type", "application/json").param("id","23")
		.when().get("api/users").then().log().all().assertThat().statusCode(404);
	}

}
