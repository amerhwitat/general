use std::sync::{Arc, RwLock};
use axum::{routing::get, Json, Router};
use serde::Serialize;
#[derive(Serialize,Clone)] struct Health { status: &'static str }
#[tokio::main] async fn main(){ let _state=Arc::new(RwLock::new(Vec::<String>::new())); let app=Router::new().route("/health",get(||async{Json(Health{status:"ok"})})); let listener=tokio::net::TcpListener::bind("0.0.0.0:8080").await.unwrap(); axum::serve(listener,app).await.unwrap(); }
