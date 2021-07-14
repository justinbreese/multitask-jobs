// Databricks notebook source
import org.apache.spark.sql.functions._
import scala.util._

// dbutils.widgets.text("savePath", "")

val savePath = dbutils.widgets.get("savePath").toString
val animal = dbutils.widgets.get("animal").toString
val food = dbutils.widgets.get("food").toString
val rawPath = savePath + "/raw"
val bronzePath = savePath + "/bronze"
val enrichedPath = savePath + "/enriched"
val silverPath = savePath + "/silver"
val goldPath = savePath + "/gold"
