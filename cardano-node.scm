(define-module (cardano-node)
  #:use-module (guix packages)
  #:use-module (guix download)
  #:use-module (guix git-download)
  #:use-module (guix build-system copy)
  #:use-module (guix licenses))

;; To download new file and get sha256sum on base32
;; guix download URL
;; to install
;; guix package -L /this dir path/ -i cardano-wallet
;;

(define-public cardano-wallet
  (package
   (name "cardano-wallet")
   (version "2023-12-18")
   (source (origin
            (method url-fetch)
            (uri "https://github.com/cardano-foundation/cardano-wallet/releases/download/v2023-12-18/cardano-wallet-v2023-12-18-linux64.tar.gz")
            (sha256
             (base32
              "0yainzgxc67kzjy9k0zvjq6ndfhwcyg0wmzka6l31rgknx071kvy"))))
   (build-system copy-build-system)
   (arguments
    '(#:install-plan
      '(("." "bin/" #:include-regexp ("cardano-" "bech32")))))
   (synopsis "cardano node, cli, address, bech32 and wallet")
   (description
    "The cardano node and wallet from iohk")
   (home-page "https://github.com/input-output-hk/cardano-wallet")
   (license asl2.0)))

(define-public cardano-node
  (package
   (name "cardano-node")
   (version "1.35.4")
   (source (origin
            (method url-fetch)
            (uri "https://hydra.iohk.io/build/21343721/download/1/cardano-node-1.35.4-linux.tar.gz")
            (sha256
             (base32
              "0csnsg75fal3h6vll02sjigm7yxv5dbjkhpr1ancc3flfkg0p7iz"))))
   (build-system copy-build-system)
   (arguments
    '(#:install-plan
      '((".." "bin/" #:include ("ledger-state" "chain-sync")))))
   (synopsis "cardano node, cli, address, bech32 and wallet")
   (description
    "The cardano node and wallet from iohk")
   (home-page "https://github.com/input-output-hk/cardano-wallet")
   (license asl2.0)))

(define-public cardano-db-sync
  (package
   (name "cardano-db-sync")
   (version "13.0.5")
   (source (origin
            (method url-fetch)
            (uri "https://hydra.iohk.io/build/19105782/download/1/cardano-db-sync-13.0.5-linux.tar.gz")
            (sha256
             (base32
              "0labymh2dnkj44s0hc47qxcg4wvhw92g45498bjgh6kx0cmwxq88"))))
   (build-system copy-build-system)
   (arguments
    '(#:install-plan
      '(("." "bin/" #:include ("cardano-db-sync")))))
   (inputs (list cardano-wallet))
   (synopsis "cardano node, cli, address, bech32 and wallet")
   (description
    "The cardano node and wallet from iohk")
   (home-page "https://github.com/input-output-hk/cardano-wallet")
   (license asl2.0)))
