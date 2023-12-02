// https://adventofcode.com/2023/day/2
import scala.io.Source
import scala.math._

object Day2 {

  def canGameExist(input: String, maximum: (Int, Int, Int)): (Int, Boolean) = {
    val gameState = input.split(":")
    val gameId = gameState.head.split(" ").last.toInt
    val invalidStateExists = gameState.last.replace(";", ",").trim.split(",").exists { combo =>
      val c = combo.trim.split(" ")
      val quantity = c.head.toInt
      val color = c.last
      if (color.contains("red"))
        maximum._1 < quantity
      else if (color.contains("green"))
        maximum._2 < quantity
      else
        maximum._3 < quantity
    }
    (gameId, !invalidStateExists)
  }

  def minimumPowerForGame(input: String): Int = {
    var rc = 0
    var gc = 0
    var bc = 0
    input.split(":").last.split(";").foreach { hand =>
      hand.split(",").foreach { combo =>
        val c = combo.trim.split(" ")
        val quantity = c.head.toInt
        val color = c.last
        if (color.contains("red"))
          rc = max(rc, quantity)
        else if (color.contains("green"))
          gc = max(gc, quantity)
        else
          bc = max(bc, quantity)
      }
    }
    rc * gc * bc
  }

  def main(args: Array[String]): Unit = {
    // Part one:
    // Format (R,G,B).
    val gameMax = (12, 13, 14)
    val source = Source.fromFile("day2.txt").getLines.toSeq

    val validGameResultSum = source.map(canGameExist(_, gameMax)).filter(_._2 == true).map(_._1).sum
    println(s"(Part one): Sum of valid game ids: ${validGameResultSum}")

    // Part two:
    val sumOfPowers = source.map(minimumPowerForGame).sum
    println(s"(Part two): Minimum power sum of games: $sumOfPowers")
  }
}
