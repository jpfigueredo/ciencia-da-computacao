#!/bin/bash  
SOURCE="/mnt/sdb1/BACKUP/Estudos/HIGHER-EDUCATION/EDS-INFNET/08-Periodo/4-Programacao_Distribuida_com_Redes_usando_Linux_e_Python[25E1_4]"
DEST_CURRENT="$HOME/backup/"  
DEST_OLD="$HOME/backup/backup_old/$(date +%Y-%m-%d_%H-%M-%S)"  

mkdir -p "$DEST_CURRENT" "$DEST_OLD"  

rsync -avh --delete --backup --backup-dir="$DEST_OLD" \  
  "$SOURCE" "$DEST_CURRENT" \  
  --exclude={'node_modules/','.venv/','*.tmp'}  

echo "Backup concluído em: $(date)" >> "$HOME/backup/backup.log"  
md5sum "$DEST_CURRENT"/* >> "$HOME/backup/backup_checksums.md5"  