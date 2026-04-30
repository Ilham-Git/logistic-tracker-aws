# Phase 1: Network Provisioning (VPC Setup)

Dokumen ini mencatat parameter konfigurasi manual (ClickOps) untuk jaringan dasar AWS sebelum dikonversi menjadi Terraform.

## 1. Virtual Private Cloud (VPC)
- **VPC Name:** `logistic-vpc-prod`
- **IPv4 CIDR Block:** `10.0.0.0/16`
- **Region:** `[TBD - Contoh: ap-southeast-1]`

## 2. Subnets
| Subnet Name | Type | Availability Zone | IPv4 CIDR Block |
|---|---|---|---|
| `public-subnet-1a` | Public | `[TBD]` | `10.0.1.0/24` |
| `public-subnet-1b` | Public | `[TBD]` | `10.0.2.0/24` |
| `private-subnet-1a` | Private | `[TBD]` | `10.0.3.0/24` |
| `private-subnet-1b` | Private | `[TBD]` | `10.0.4.0/24` |

## 3. Internet Gateway (IGW)
- **IGW Name:** `logistic-igw-prod`
- **Attached to VPC:** `logistic-vpc-prod`

## 4. Route Tables
- **Public Route Table:** Mengarahkan traffic `0.0.0.0/0` ke `logistic-igw-prod`.
- **Private Route Table:** `[Local only / TBD NAT Gateway]`

---
*Catatan: Screenshot topologi akan ditambahkan ke folder images/ setelah provisioning selesai.*