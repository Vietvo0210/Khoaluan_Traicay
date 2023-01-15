-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th1 15, 2023 lúc 09:26 AM
-- Phiên bản máy phục vụ: 10.4.24-MariaDB
-- Phiên bản PHP: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `fruits`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `admin`
--

CREATE TABLE `admin` (
  `id` int(11) NOT NULL,
  `name` varchar(20) DEFAULT NULL,
  `email` varchar(30) NOT NULL,
  `password` varchar(32) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Đang đổ dữ liệu cho bảng `admin`
--

INSERT INTO `admin` (`id`, `name`, `email`, `password`) VALUES
(1, 'Admin', 'admin@hufi.vn', 'Admin1');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Đang đổ dữ liệu cho bảng `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `customer`
--

CREATE TABLE `customer` (
  `id` int(11) NOT NULL,
  `fullname` varchar(50) DEFAULT NULL,
  `email` varchar(150) DEFAULT NULL,
  `phone_number` varchar(20) DEFAULT NULL,
  `address` varchar(200) DEFAULT NULL,
  `password` varchar(32) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Đang đổ dữ liệu cho bảng `customer`
--

INSERT INTO `customer` (`id`, `fullname`, `email`, `phone_number`, `address`, `password`) VALUES
(1, 'huy', 'thanvhuy38@gmial.com', '0944332653', 'ha tinh', 'Huy.202'),
(2, 'viet', 'thanvhuy38@gmial.com', '0944332653', 'ha tinh', 'viet123'),
(3, 'doan', 'thanvhuy38@gmail.com', '0944332653', 'ha tinh', 'vhd1234');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Đang đổ dữ liệu cho bảng `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Đang đổ dữ liệu cho bảng `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2022-11-25 03:57:13.378446'),
(2, 'auth', '0001_initial', '2022-11-25 03:57:14.461541'),
(3, 'admin', '0001_initial', '2022-11-25 03:57:14.706103'),
(4, 'admin', '0002_logentry_remove_auto_add', '2022-11-25 03:57:14.762260'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2022-11-25 03:57:14.780249'),
(6, 'contenttypes', '0002_remove_content_type_name', '2022-11-25 03:57:14.914600'),
(7, 'auth', '0002_alter_permission_name_max_length', '2022-11-25 03:57:15.075952'),
(8, 'auth', '0003_alter_user_email_max_length', '2022-11-25 03:57:15.116919'),
(9, 'auth', '0004_alter_user_username_opts', '2022-11-25 03:57:15.137420'),
(10, 'auth', '0005_alter_user_last_login_null', '2022-11-25 03:57:15.234645'),
(11, 'auth', '0006_require_contenttypes_0002', '2022-11-25 03:57:15.242640'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2022-11-25 03:57:15.265628'),
(13, 'auth', '0008_alter_user_username_max_length', '2022-11-25 03:57:15.306605'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2022-11-25 03:57:15.345581'),
(15, 'auth', '0010_alter_group_name_max_length', '2022-11-25 03:57:15.377563'),
(16, 'auth', '0011_update_proxy_permissions', '2022-11-25 03:57:15.391590'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2022-11-25 03:57:15.419577'),
(18, 'sessions', '0001_initial', '2022-11-25 03:57:15.489353');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `feedback`
--

CREATE TABLE `feedback` (
  `id` int(11) NOT NULL,
  `firstname` varchar(30) DEFAULT NULL,
  `lastname` varchar(30) DEFAULT NULL,
  `email` varchar(250) DEFAULT NULL,
  `phone_number` varchar(20) DEFAULT NULL,
  `note` varchar(1000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Đang đổ dữ liệu cho bảng `feedback`
--

INSERT INTO `feedback` (`id`, `firstname`, `lastname`, `email`, `phone_number`, `note`) VALUES
(1, 'than', 'van huy', 'doan@gmail.com', '093882323', 'gia nay chua qua'),
(3, 'vo', 'viet ', 'viet@gmail.com\r\n', '093882323', 'gia nay chua qua');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `galery`
--

CREATE TABLE `galery` (
  `id` int(11) NOT NULL,
  `product_id` int(11) DEFAULT NULL,
  `thumbnail` varchar(500) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Đang đổ dữ liệu cho bảng `galery`
--

INSERT INTO `galery` (`id`, `product_id`, `thumbnail`) VALUES
(1, 1, '[C;img]'),
(3, 2, '[C;img]');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `orders`
--

CREATE TABLE `orders` (
  `id` int(11) NOT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `fullname` varchar(50) DEFAULT NULL,
  `email` varchar(150) DEFAULT NULL,
  `phone_number` varchar(20) DEFAULT NULL,
  `address` varchar(200) DEFAULT NULL,
  `note` varchar(1000) DEFAULT NULL,
  `order_date` varchar(15) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `total_money` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Đang đổ dữ liệu cho bảng `orders`
--

INSERT INTO `orders` (`id`, `customer_id`, `fullname`, `email`, `phone_number`, `address`, `note`, `order_date`, `status`, `total_money`) VALUES
(1, 4, 'huy', 'hoang@gmail.com', '095533234', 'Ha tinh', 'giao gio hanh chinh nha', '02/02/2022', 0, 120200),
(3, 1, 'doan', 'doan@gmail.com', '0923442355', 'ht 02', 'value-7', '02/02/2022', 0, 120200),
(4, 0, 'viet', '[value-4]', '[value-5]', '[value-6]', '[value-7]', '02/09/2023', 0, 123000),
(5, 1, 'huy', 'hu@GMIAL', '02348', 'SADF', 'SDF', '02/09/2001', 0, 12000),
(6, 2, 'Thân Văn', 'thanvhuy38@gmail.com', '0944332653', 'hla', 'D', '02/09/2001', 0, 213);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `order_details`
--

CREATE TABLE `order_details` (
  `id` int(11) NOT NULL,
  `order_id` int(11) DEFAULT NULL,
  `product_id` int(11) DEFAULT NULL,
  `price` int(11) DEFAULT NULL,
  `num` int(11) DEFAULT NULL,
  `total_money` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Đang đổ dữ liệu cho bảng `order_details`
--

INSERT INTO `order_details` (`id`, `order_id`, `product_id`, `price`, `num`, `total_money`) VALUES
(1, 0, 0, 0, 0, 0),
(2, 2, 2, 2000, 4, 80000);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `product`
--

CREATE TABLE `product` (
  `id` int(11) NOT NULL,
  `title` varchar(250) DEFAULT NULL,
  `price` float DEFAULT NULL,
  `discount` float DEFAULT NULL,
  `thumbnail` varchar(500) DEFAULT NULL,
  `description` varchar(2000) CHARACTER SET utf8 DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Đang đổ dữ liệu cho bảng `product`
--

INSERT INTO `product` (`id`, `title`, `price`, `discount`, `thumbnail`, `description`) VALUES
(1, 'asd', 1212, 12, 'https://i.ibb.co/HBydxff/xoai.jpg', 'sdf'),
(2, 'Xoài', 25000, 0, 'https://i.ibb.co/HBydxff/xoai.jpg', 'Xoài có chứa phenol (những hợp chất hữu cơ mà phân tử của chúng có nhóm hidroxyl liên kết trực tiếp với nguyên tử cacbon của vòng benzene), chẳng hạn như quercetin, isoquercitrin, astragalin, fisetin, axít galic, methylgallat và enzim có khả năng ngăn ngừa bệnh ung thư.  Ngoài ra, xoài còn chứa rất nhiều chất xơ hòa tan trong nước được biết đến như là pectin. Các nhà khoa học cho rằng việc ăn nhiều chất xơ sẽ giúp giảm thiểu nguy cơ mắc bệnh ung thư về đường tiêu hóa. Khoảng 165g xoài sẽ cung cấp cho cơ thể chúng ta tới 75% lượng vitamin C cần thiết hằng ngày. Xoài cũng cung cấp một lượng chất chống oxy hóa mạnh mẽ, giúp bảo vệ các tế bào không bị các gốc tự do hủy hoại, đồng thời giảm thiểu nguy cơ mắc bệnh ung thư.'),
(3, 'Vải thiều', 40000, 0, 'https://i.ibb.co/x23TfGQ/vai-thieu.jpg', 'Vải thiều (quả vải) còn có một cái tên khác chính là Lệ chi, nó thuộc họ Bồ hòn, có tên khoa học chính là Litchi chinensis và tên tiếng anh chính là Lychee.  Đây như một loại cây nhiệt đới có xuất xứ từ những tỉnh Quảng Đông và Phúc Kiến, Trung Quốc. Thân cây có thể cao đến khoảng 15 – 20m, lá hình lông chim, mọc so le và nhiều lá chét. Những lá non mới mọc có màu đỏ đồng sáng, sau dần chuyển sang màu xanh lúc đạt đến kích thước cực đại.cho sức khỏe và có hương vị ngon ngọt.  Khi vào hè chắc ai cũng thích loại hoa quả vải thiều, một loại hoa quả có vị ngọt thanh thanh ngon tuyệt vời. Nó là hoa quả mang nhiều tác dụng tuyệt vời cho sức khỏe của mọi người nên nó được nhiều người thích. Vải thiều Thanh Hà và vải thiều Lục Ngạn là nổi tiếng nhất. Bạn muốn hiểu hơn về loại quả này bạn hãy đọc bài viết sau đây nhé!  Mục lục Vải thiểu là gì? Vải thiều ở đâu ngon nhất? Vải thiều Thanh Hà, Hải Dương Vải thiều Lục Ngạn, Bắc Giang Giá vải thiều Vải thiều làm món gì ngon? Vải sấy khô Chè vải hạt sen Kem vải Lời kết Vải thiểu là gì? Vải thiều (quả vải) còn có một cái tên khác chính là Lệ chi, nó thuộc họ Bồ hòn, có tên khoa học chính là Litchi chinensis và tên tiếng anh chính là Lychee.  Đây như một loại cây nhiệt đới có xuất xứ từ những tỉnh Quảng Đông và Phúc Kiến, Trung Quốc. Thân cây có thể cao đến khoảng 15 – 20m, lá hình lông chim, mọc so le và nhiều lá chét. Những lá non mới mọc có màu đỏ đồng sáng, sau dần chuyển sang màu xanh lúc đạt đến kích thước cực đại.    Hoa nhỏ màu trắng ánh xanh lục hay trắng ánh vàng, mọc thành những chùm có thể dài đến 30cm và có mùi thơm vô cùng thú vị, đặc biệt.  Quả vải thuộc loại quả hạch, hình cầu, hình trứng tới hình trái tim. Nó có vỏ mỏng, dai và có màu xanh lục lúc nó còn non sau dần chuyển sang màu đỏ hay đỏ hồng lúc nó đã chín, bề mặt vỏ sần sùi. Thịt quả có màu trắng trong, bao quanh một hạt màu nâu sẫm. Kích thước và vị của nó sẽ dựa vào vị trí địa lý và giống.'),
(4, 'Mảng cầu na', 50000, 0, 'https://i.ibb.co/z5bpP81/mangcau-Na-1.jpg', 'Quả na còn gọi là mãng cầu ta, mãng cầu dai, phan lệ chi. Là quả của cây na có tên khoa học là Annona squamosa. Thuộc họ Mãng cầu Annonaceae. Quả na còn có tên tiếng anh là Sugar apple hay Sweetsop. Đây là loại trái cây thơm ngon, phổ biến và hấp dẫn cho thịt quả ngon, ngọt khi chín.Cây na thuộc loại cây gỗ nhỏ. Cao khoảng 3-8m. Thân ngắn, tán rộng, các nhánh phân tán không đều. Lá mọc xen kẽ, cuống lá dài. Lá có hình elip hoặc hình mác, đỉnh nhọn đến tù, đáy rộng. Cụm hoa gồm các hoa đơn độc. Hoa thơm có màu xanh lục đến vàng. Quả na là dạng quả tụ, mỗi lá noãn sẽ phát triển thành 1 quả mọng. Tất cả những quả này dính với nhau thành một khối hình tim, hình cầu. Mặt ngoài trái na có hình màu xanh, nhiều rãnh. Đường kính 6-10cm. Quả thơm, ngọt và có màu trắng đến vàng nhạt. Hạt bóng, hình thuôn dài và nhẵn, màu nâu sẫm đến đen. Kích thước từ 1.3-1.6 cm. Hạt chứa độc tố, có thể làm bỏng da và trừ sâu bọ, chấy rận.'),
(5, 'Chôm chôm', 23003, 39, 'https://i.ibb.co/6XD4LTZ/chomchom-1.png', 'Chôm chôm là loại trái cây có giá trị dinh dưỡng cao (chứa nhiều vitamin C, giàu đạm, chất béo và các nguyên tố vi lượng như đồng, mangan, kali, canxi, sắt...) và trái chôm chôm còn được dung làm thuốc chữa bệnh.  Chôm chôm là loài cây có quả hoặc để ăn tươi, hoặc đóng hộp dưới nhiều hình thức, để dự trữ hoặc xuất khẩu. Hạt chôm chôm có thành phần dầu cao nên cũng được dùng để sản xuất dầu ăn hay xà phòng. Cây và rễ chôm chôm cũng có thể dùng cho việc sản xuất dược phẩm và màu. Ở Việt Nam, người làm vườn chôm chôm có mức thu nhập tương đối cao so với các ngành trồng trọt khác.  Hạt chôm chôm chứa 35 - 40% chất dầu béo đặc, có cấu trúc của hạt ca cao, có mùi dễ chịu, gồm phần lớn là arachidin, cùng với olein và stearin. Vỏ cây và quả xanh có chứa tanin.  Vỏ chôm chôm chứa nhiều tanin, chữa ỉa chảy, kiết lỵ, sốt... với liều 20 - 30g. Hạt chôm chôm, còn gọi là thiều tử, vị ngọt, tính ấm, chứa nhiều chất béo không no, có tác dụng tiêu viêm kháng khuẩn, dùng chữa viêm niêm mạc miệng, kiết lỵ, hỗ trợ điều trị tiểu đường, các vết loét lâu ngày, điều chỉnh lipid máu, giảm béo và làm đẹp da. Chôm chôm là loại trái rất thích hợp cho những người bị vữa xơ động mạch, cao huyết áp, tăng đường huyết... Tuy nhiên, vì chứa nhiều chất béo nên nếu ăn quá nhiều hạt chôm chôm có thể xuất hiện cảm giác say say và gây buồn nôn, đầy bụng.  Ngoài ra, có thể dùng áo hạt để ăn vì nó rất bổ và có chức năng giải nhiệt'),
(6, 'Xoài', 23003, 39, 'https://i.ibb.co/HBydxff/xoai.jpg', 'Xoài có chứa phenol (những hợp chất hữu cơ mà phân tử của chúng có nhóm hidroxyl liên kết trực tiếp với nguyên tử cacbon của vòng benzene), chẳng hạn như quercetin, isoquercitrin, astragalin, fisetin, axít galic, methylgallat và enzim có khả năng ngăn ngừa bệnh ung thư.');

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`);

--
-- Chỉ mục cho bảng `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Chỉ mục cho bảng `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Chỉ mục cho bảng `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Chỉ mục cho bảng `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Chỉ mục cho bảng `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Chỉ mục cho bảng `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Chỉ mục cho bảng `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`id`);

--
-- Chỉ mục cho bảng `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Chỉ mục cho bảng `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Chỉ mục cho bảng `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Chỉ mục cho bảng `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Chỉ mục cho bảng `feedback`
--
ALTER TABLE `feedback`
  ADD PRIMARY KEY (`id`);

--
-- Chỉ mục cho bảng `galery`
--
ALTER TABLE `galery`
  ADD PRIMARY KEY (`id`);

--
-- Chỉ mục cho bảng `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`id`);

--
-- Chỉ mục cho bảng `order_details`
--
ALTER TABLE `order_details`
  ADD PRIMARY KEY (`id`);

--
-- Chỉ mục cho bảng `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT cho bảng `customer`
--
ALTER TABLE `customer`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT cho bảng `feedback`
--
ALTER TABLE `feedback`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT cho bảng `galery`
--
ALTER TABLE `galery`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT cho bảng `orders`
--
ALTER TABLE `orders`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT cho bảng `order_details`
--
ALTER TABLE `order_details`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT cho bảng `product`
--
ALTER TABLE `product`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
