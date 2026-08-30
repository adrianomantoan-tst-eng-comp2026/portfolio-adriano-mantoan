package com.autostock.controller;

import java.math.BigDecimal;
import java.util.List;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import com.autostock.model.StatusVeiculo;
import com.autostock.model.Veiculo;
import com.autostock.service.VeiculoService;
import jakarta.validation.Valid;

@RestController @RequestMapping("/api/veiculos")
public class VeiculoController {
    private final VeiculoService service;
    public VeiculoController(VeiculoService service) { this.service = service; }
    @GetMapping public List<Veiculo> listar() { return service.listarTodos(); }
    @GetMapping("/{id}") public Veiculo buscar(@PathVariable Long id) { return service.buscarPorId(id); }
    @PostMapping public ResponseEntity<Veiculo> cadastrar(@Valid @RequestBody Veiculo v) { return ResponseEntity.status(HttpStatus.CREATED).body(service.salvar(v)); }
    @PutMapping("/{id}") public Veiculo atualizar(@PathVariable Long id, @Valid @RequestBody Veiculo v) { return service.atualizar(id, v); }
    @DeleteMapping("/{id}") public ResponseEntity<Void> excluir(@PathVariable Long id) { service.excluir(id); return ResponseEntity.noContent().build(); }
    @GetMapping("/pesquisar")
    public List<Veiculo> pesquisar(@RequestParam(required=false) Long marcaId, @RequestParam(required=false) Long modeloId, @RequestParam(required=false) StatusVeiculo status, @RequestParam(required=false) Integer ano, @RequestParam(required=false) BigDecimal precoMinimo, @RequestParam(required=false) BigDecimal precoMaximo) {
        return service.filtrar(marcaId, modeloId, status, ano, precoMinimo, precoMaximo);
    }
}
