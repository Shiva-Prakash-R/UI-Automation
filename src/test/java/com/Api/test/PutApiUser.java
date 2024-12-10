package com.Api.test;

import static io.restassured.RestAssured.given;

import io.restassured.RestAssured;
import io.restassured.path.json.JsonPath;

public class PutApiUser {
	
public static void main(String[] args) {
		
	
		RestAssured.baseURI = "https://reqres.in/";
		
		// Update Record using String in Json body:
		
		String Name = "morpheus New Name";
		
		String Job = "zion resident Job";
		
		given().log().all().header("Content-Type", "application/json").body("{\r\n"
				+ "    \"name\": \""+Name+"\",\r\n"
				+ "    \"job\": \""+Job+"\"\r\n"
				+ "}")
		.when().put("api/users/2").then().log().all().assertThat().statusCode(200);
		
	}

		


}
