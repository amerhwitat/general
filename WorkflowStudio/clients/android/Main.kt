package com.amerhwitat.chimeraworkflow

data class Project(val id:String,val name:String,val methodology:String="scrum")
object WorkflowClient { fun health():String = "ok" }
fun main(){ println("Chimera WorkFlow Android/Kotlin client foundation") }
