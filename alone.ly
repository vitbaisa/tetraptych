\version "2.12.2"

upper = \relative c' {
  \tempo 4 = 60
  \clef treble
  \key g \minor
  \time 3/4

  <g'' bes d>4 <d g bes>2
  <g, bes d>4 <d g bes>2

  \bar "|."
}

lower = \relative c {
  \clef bass
  \key g \minor
  \time 3/4

  <g g'>2.\sustainOn
  <g, g'>2.\sustainOff\sustainOn
  
}

\header {}

\score {
  \new PianoStaff <<
    \new Staff \upper
    \new Staff \lower
  >>
  \layout {}
  \midi {}
}

\paper {
  paper-width = 20\cm
  paper-height = 7\cm
  print-page-number = ##f
  indent = 0\cm
}
