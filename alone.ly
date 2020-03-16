\version "2.18.2"

upper = \relative c' {
  \clef treble
  \key g \minor
  \time 4/4

  <g' bes d>4\f\> <d a' c>2.
  <d g bes>4\arpeggio <c es a>2.
  <bes d g>4\!\mp <a d f>2.\fermata
  <g' bes d>4\f\> <d a' c>2.
  <d g bes>4 <c es a>2.\!
  <c d~ g~>1
  <b d g>1

  \partial 4 c8 d
  \key c \major
  \time 3/4

  <d e g>8 c16 <d e g>8 c16 <d e g>8 b4
  <d e g>8 c16 <d e g>8 c16 <d e g>8 b8 a
  <d e g>8 c16 <d e g>8 c16 <d e g>8 b4
  <d e g>8 c16 <d e g>8 c16 <d e g>8 b8 a
  <c d g>8 b16 <c d g>8 b16 <c d g>8 b4
  <c d f>8 b16 <c d f>8 b16 <c d f>8 b8 a
  <c d f>8 b16 <c d f>8 b16 <c d f>8 b4
  <c d f>8 b16 <c d f>8 b16 <c d f>8 b8 a

  <d e g>8 c16 <d e g>8 c16 <d e g>8 b4
  <d e g>8 c16 <d e g>8 c16 <d e g>8 b8 a
  <d e g>8 c16 <d e g>8 c16 <d e g>8 b4
  <d e g>8 c16 <d e g>8 c16 <d e g>8 b8 a
  <c d f>8 b16 <c d f>8 b16 <c d f>8 b4
  <c d f>8 b16 <c d f>8 b16 <c d f>8 b8 a
  <c d f>8 b16 <c d f>8 b16 <c d f>8 b4
  <c d f>8 b16 <c d f>8 b16 <c d f>8 b8 a

  <b c f>8 a16 <b c f>8 a16 <b c f>8 a4
  <b c e>8 a16 <b c e>8 a16 <b c e>8 a8 g
  <b c e>8 a16 <b c e>8 a16 <b c e>8 a4
  <b c e>8 a16 <b c e>8 a16 <b c e>8 <c d~ f~>8 <b d f>

  <d e g>8 c16 <d e g>8 c16 <d e g>8 b4
  <d e g>8 c16 <d e g>8 c16 <d e g>8 b8 a
  <d e g>8 c16 <d e g>8 c16 <d e g>8 b4
  <d e g>8_\markup{\italic rit.} c16 <d e g>8 c16 <d e g>8 b4\fermata

  \time 4/4
  e2\arpeggio\afterGrace fis\trill { e32[ fis] }
  g2\arpeggio d
  d\arpeggio\afterGrace e\trill { d32[ e] }
  f2\arpeggio c
  c\arpeggio\afterGrace d\trill { c32[ d] }
  e4.\arpeggio c8 f\< e d c\f\!
  d1\arpeggio\p

  e4.\mf\arpeggio e8\afterGrace fis2\trill { e32[ fis] }
  g4.\arpeggio d8 d2
  d4.\arpeggio d8\afterGrace e2\trill { d32[ e] }
  f4.\arpeggio c8 c2
  c4.\arpeggio c8\afterGrace d2\trill { c32[ d] }
  e4.\arpeggio c8 f\< e d c\f\!
  d1\arpeggio\p

  <c e>2\mf\arpeggio <d fis>\sf

  \key g \minor

  <g bes d>4\arpeggio\f\> <d a' c>2.
  <d g bes>4\arpeggio <c es a>2.
  <bes d g>4\!\mp <a d f>2.\fermata
  <g' bes d>4\f\> <d a' c>2.
  <d g bes>4 <c es a>2.\!
  <c d~ g~>1\fermata
  <b d g>\fermata

  \bar "|."
}

lower = \relative c {
  \clef bass
  \key g \minor
  \time 4/4

  <g g'>1
  <g, g'>\arpeggio
  <g' g'>4 <d d'>2.\fermata
  <es es'>1
  <e e'>4 <f f'>2.
  <g g'>1~
  <g g'>

  \partial 4 r4
  \key c \major
  \time 3/4

  <c g'>2.\sustainOn
  <c g'>2.\sustainOff\sustainOn
  <c g'>2.\sustainOff_\markup{\italic simile}
  <c g'>2.
  <g g'>2.
  <g g'>2.
  <g g'>2.
  <g g'>2.
  <c g'>2.
  <c g'>2.
  <c g'>2.
  <c g'>2.
  <g g'>2.
  <g g'>2.
  <g g'>2.
  <g g'>2 r8 b
  <f f'>2.
  <f f'>2.
  <f f'>2.
  <f f'>2 <g g'>4
  <c g'>2.
  <c g'>2.
  <c g'>2.
  <c g'>2.

  \time 4/4
  <c g'>1\arpeggio
  <b g'>\arpeggio
  <bes g'>\arpeggio
  <a f'>\arpeggio
  <as f'>\arpeggio
  <g e'>2\arpeggio <d d'>8 <e e'> <f f'> <fis fis'>
  <g g'>1\arpeggio
  
  <c g'>1\arpeggio
  <b g'>\arpeggio
  <bes g'>\arpeggio
  <a f'>\arpeggio
  <as f'>\arpeggio
  <g e'>2\arpeggio <d d'>8 <e e'> <f f'> <fis fis'>
  <g g'>2\arpeggio f

  <c' g'>1\arpeggio

  \key g \minor

  <g g'>1
  <g, g'>
  <g' g'>4 <d d'>2.\fermata
  <es es'>1
  <e e'>4 <f f'>2.
  <g g'>1~\fermata
  <g g'>\fermata
}

\header {
  tagline = ""
}

\score {
  \new PianoStaff <<
    \set PianoStaff.connectArpeggios = ##t
    \new Staff \upper
    \new Staff \lower
  >>
  \layout {
    \context {
      \Score
      \omit BarNumber
    }
  }
  \midi {}
}

\paper {
  paper-width = 200\cm
  paper-height = 7\cm
  print-page-number = ##f
  indent = 0\cm
}
