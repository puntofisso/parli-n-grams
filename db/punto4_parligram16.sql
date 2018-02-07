-- phpMyAdmin SQL Dump
-- version 4.7.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Dec 07, 2017 at 06:40 AM
-- Server version: 5.6.38
-- PHP Version: 5.6.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `punto4_parligram16`
--
CREATE DATABASE IF NOT EXISTS `punto4_parligram16` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `punto4_parligram16`;

-- --------------------------------------------------------

--
-- Table structure for table `logs`
--

DROP TABLE IF EXISTS `logs`;
CREATE TABLE `logs` (
  `id` int(20) NOT NULL,
  `ngrams` text COLLATE utf8_unicode_ci NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `mp` varchar(100) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `ngrams`
--

DROP TABLE IF EXISTS `ngrams`;
CREATE TABLE `ngrams` (
  `ngram` varchar(120) COLLATE utf8_unicode_ci NOT NULL,
  `year` int(4) NOT NULL,
  `count` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `ngrams.bak`
--

DROP TABLE IF EXISTS `ngrams.bak`;
CREATE TABLE `ngrams.bak` (
  `ngram` varchar(120) COLLATE utf8_unicode_ci NOT NULL,
  `year` int(4) NOT NULL,
  `count` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `ngramsmp`
--

DROP TABLE IF EXISTS `ngramsmp`;
CREATE TABLE `ngramsmp` (
  `ngram` varchar(120) COLLATE utf8_unicode_ci NOT NULL,
  `mp` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `year` int(4) NOT NULL,
  `count` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `yearcounts`
--

DROP TABLE IF EXISTS `yearcounts`;
CREATE TABLE `yearcounts` (
  `year` int(4) NOT NULL,
  `count` int(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `yearcounts.bak`
--

DROP TABLE IF EXISTS `yearcounts.bak`;
CREATE TABLE `yearcounts.bak` (
  `year` int(4) NOT NULL,
  `count` int(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `yearcountsmp`
--

DROP TABLE IF EXISTS `yearcountsmp`;
CREATE TABLE `yearcountsmp` (
  `year` int(4) NOT NULL,
  `mp` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `count` int(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

DROP TABLE IF EXISTS `updatestring`;
CREATE TABLE `updatestring` (
  `string` varchar(100) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;




--
-- Indexes for dumped tables
--

--
-- Indexes for table `logs`
--
ALTER TABLE `logs`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `ngrams`
--
ALTER TABLE `ngrams`
  ADD KEY `idx` (`ngram`,`year`);

--
-- Indexes for table `ngrams.bak`
--
ALTER TABLE `ngrams.bak`
  ADD KEY `idx` (`ngram`,`year`);

--
-- Indexes for table `ngramsmp`
--
ALTER TABLE `ngramsmp`
  ADD KEY `idx` (`ngram`,`year`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `logs`
--
ALTER TABLE `logs`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8670;COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
