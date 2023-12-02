// https://adventofcode.com/2023/day/1
import scala.io.Source
import scala.util.matching.Regex

object Day1 {

  val digitMap = Map('1' -> 1, '2' -> 2, '3' -> 3, '4' -> 4, '5' -> 5, '6' -> 6, '7' -> 7, '8' -> 8, '9' -> 9, '0' -> 0)
  val digitAlphaMap = Map(
    "one" -> 1,
    "two" -> 2,
    "three" -> 3,
    "four" -> 4,
    "five" -> 5,
    "six" -> 6,
    "seven" -> 7,
    "eight" -> 8,
    "nine" -> 9,
    "zero" -> 0,
  )

  def parseCalibrationLine(input: String): Int = {
    val numericInput = input.trim.filter(_.isDigit)
    digitMap(numericInput.head) * 10 + digitMap(numericInput.last)
  }

  def parseInclusiveCalibrationLine(input: String, digitsRegex: Regex, allDigitsMap: Map[String, Int]): Int = {
    val matchIterations = for {
      inputTail <- input.tails
      oneMatch <- digitsRegex.findPrefixOf(inputTail.trim)
    } yield oneMatch
    val allMatches = matchIterations.toSeq
    allDigitsMap(allMatches.head) * 10 + allDigitsMap(allMatches.last)
  }

  def main(args: Array[String]): Unit = {
    val source = Source.fromFile("day1.txt").getLines.toSeq
    // Part One:
    val parsedCalibrationLines = source.map(parseCalibrationLine)
    val res = parsedCalibrationLines.foldLeft(0)(_ + _)
    println(s"(Part one): Total calibration number: ${res}")

    // Part Two:
    val allDigitsMap = digitAlphaMap ++ (0 to 9).map(n => n.toString -> n)
    // Make all iterations separated by |.
    val digitsRegex = allDigitsMap.keysIterator.mkString("|").r
    val parsedInclusiveCalibrationLines = source.map(parseInclusiveCalibrationLine(_, digitsRegex, allDigitsMap))
    val resInclusive = parsedInclusiveCalibrationLines.foldLeft(0)(_ + _)
    println(s"(Part two): Total inclusive calibration number: ${resInclusive}")
  }
}
