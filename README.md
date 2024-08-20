# Implementasi DFS untuk permainan Queens
> Seleksi Lab Ilmu Rekayasa dan Komputasi (IRK)

## **Daftar Isi**

- [Author](#author)
- [Deskripsi Program](#deskripsi-program)
- [Requirement Program](#requirements-program)
- [Set Up dan Build Program](#set-up-dan-build-program)
- [Cara Menggunakan Program](#cara-menggunakan-program)
- [Home Page](#home-page)
- [Test](#test)

## **Author**

|   NIM    |           Nama           |
| :------: | :----------------------: |
| 13522110 | Marvin Scifo Y. Hutahaean  |

## **Deskripsi Program**

<p align="justify">
Aplikasi ini adalah aplikasi permainan Queens yang dimulai dengan mengunggah file .txt sebagai data-data yang dibutuhkan untuk membuat <i>boardgame</i> yang diinginkan. Setelah itu, tombol "Solve" bisa ditekan untuk mencari posisi yang cocok untuk meletakkan Queen/Rook/Knight/Bishop agar tidak memakan satu sama lain. Tombol "Resize" juga bisa ditekan untuk memperbesar <i>boardgame</i>. Jika tidak terdapat solusi, maka akan diberikan pesan bahwa solusi tidak bisa ditemukan dan sebaliknya akan memunculkan piece di posisi-posisi yang membuat <i>piece</i> tidak memakan satu sama lain.

</p>

## **Tech Stack**
1. Python

## **Algoritma dan Penjelasannya**
Algoritma yang digunakan dalam aplikasi ini adalah DFS. DFS adalah pencarian secara mendalam. Namun tidak semua kemungkinan akan dicari. Jika terdapat bagian yang terkena "X", bagian tersebut akan dihindari dan jika bagian tersebut membuat bagian lainnya juga terkena "X", maka bagian tersebut tidak akan ditelusuri lagi. Hal ini dilakukan sampai solusi ditemukan atau semua kemungkinan dicari.

## **Cara Menggunakan Program** ##
1. Pastikan mempunyai Python 3. Karena aplikasi ini dibuat di Python 3.12, direkomendasikan mempunyai Python 3.12 juga
2. Tekan tombol "Upload File" untuk mengunggah file .txt
3. Tekan tombol "Solve" untuk melihat hasil
4. Tekan tombol "Resize" untuk mengganti ukuran papan
5. Enjoy!!!

## **Bonus**
Bonus yang diimplementasikan ada 2:
1. Penggantian ukuran papan
2. Chess Piece

<!-- Optional -->
<!-- ## License -->
<!-- This project is open source and available under the [... License](). -->

<!-- You don't have to include all sections - just the one's relevant to your project -->
